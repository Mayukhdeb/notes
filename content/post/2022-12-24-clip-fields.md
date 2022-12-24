+++
title = "CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory"
date = "2022-12-24"
author = "Mayukh Deb"
tags = ["paper"]
+++

## What are they doing?

They found a way to help a robot make a "map" of the world around it in terms of multimodal scene encodings. Then they store these multimodal scene encodings and their respective labels ("chair") on a database which is differentiable and is also easily searchable.

## How are they doing it?

1. In order to collect data, they used an RGB-D from which the following data was collected:

- RGB-D data
- bounding boxes from pre-trained object detector
    - the labels of the bounding boxes are fed into a BERT
    - the bounding boxes on the image are used to crop it and feed each crop into CLIP and store the CLIP encoding
- Spatial location (x, y, z)

They used an iphone 13 pro with a LiDAR sensor for depth image sequences.

2. Robot execution pipeline [as seen here](https://github.com/notmahi/clip-fields/blob/main/demo/4%20-%20test%20model.ipynb)

- When the robot gets a new text query, first we feed it through the SBERT (sentence BERT) and then also through CLIP
- SBERT gives us the semantic part of the query
- CLIP gives us the vision-aligned encoding

The robot then looks through it's database and finds which data-point is such that there is max similarity between the semantic representation and the visually aligned encoding.

Let us walk through some part of the code that the author wrote. Read the comments given below along with the code: 

This is where they generate encodings from a given text query from the model.

```python
def calculate_clip_and_st_embeddings_for_queries(queries):
    ## queries is a string which first gets tokenized
    all_clip_queries = clip.tokenize(queries)
    with torch.no_grad():

        ## encode text with CLIP to get "visually aligned" encoding
        all_clip_tokens = model.encode_text(all_clip_queries.to(DEVICE)).float()
        ## normalize encodings, dont exactly know why. Maybe they just want the directional information, kinda like a unit vector.
        all_clip_tokens = F.normalize(all_clip_tokens, p=2, dim=-1)

        ## encode text with SBERT to get a nice text encoding (idk semantic?)
        all_st_tokens = torch.from_numpy(sentence_model.encode(queries))
        ## normalize encodings, dont exactly know why. Maybe they just want the directional information, kinda like a unit vector.
        all_st_tokens = F.normalize(all_st_tokens, p=2, dim=-1).to(DEVICE)

    return all_clip_tokens, all_st_tokens

query = "Warm up my lunch"
clip_text_tokens, st_text_tokens = calculate_clip_and_st_embeddings_for_queries([query])
print("query =", query)
print("tokens shape =", clip_text_tokens.shape)
```

This is where they use the multimodal encodings from the query to perform a search in the robot's memory:

```python
def find_alignment_over_model(label_model, queries, dataloader, visual=False):
    ## This is the fn that we just discussed about
    clip_text_tokens, st_text_tokens = calculate_clip_and_st_embeddings_for_queries(queries)

    # We give different weights to visual and semantic alignment 
    # for different types of queries
    if visual:
        vision_weight = 10.0
        text_weight = 1.0
    else:
        vision_weight = 1.0
        text_weight = 10.0
    point_opacity = []

    ## iterate over the entire dataset (wow thats gonna be computationally expensive)
    with torch.no_grad():
        for data in tqdm.tqdm(dataloader, total=len(dataloader)):
            # Find alignmnents with the vectors

            ## for a single dataset instance, we generate the semantic and the visual encodings and normalise them
            predicted_label_latents, predicted_image_latents = label_model(data.to(DEVICE))
            data_text_tokens = F.normalize(predicted_label_latents, p=2, dim=-1).to(DEVICE)
            data_visual_tokens = F.normalize(predicted_image_latents, p=2, dim=-1).to(DEVICE)


            ## note that similarity = dot product
            ## calculate similarity between query text encoding and dataset instance label encoding
            text_alignment = data_text_tokens @ st_text_tokens.T

            ## calculate similarity between query visual encoding and dataset instance CLIP encoding 
            visual_alignment = data_visual_tokens @ clip_text_tokens.T

            ## some sort of a weighted sum to prioritize one over the other
            total_alignment = (text_weight * text_alignment) + (vision_weight * visual_alignment)
            total_alignment /= (text_weight + vision_weight)

            ## append all of these weighted similarity scores into a list
            point_opacity.append(total_alignment)

    point_opacity = torch.cat(point_opacity).T
    print(point_opacity.shape)
    return point_opacity
```

Dot product is the same as taking the cosine similarity between the query and the point embeddings.

## My opinions/further discussion

- What do we do for super large spaces with lots of stuff? The dataset would become very large and then it would probably not be practical to run over the entire dataset in real-time. A possible solution (given that we have enough storage) is to pre-compute the dataset embeddings and then query them when required for calculating the similarity score. Problem is that even this will take up tons of storage. Probably makes sense to keep the big stuff "on the cloud" and send the queries from the humans via an API to the servers first and then return the results to the robot.

- Can we then also teach this robot to "look for my car keys"? Given that the car keys are beyond the "dataset" of the robot. We can ask it to keep searching for objects in the home and then when it gets a high similarity score for "car keys" for a given weighted query encoding then we return the result to the user saying that "this might be what you're looking for."

- Okay so what's a cheap way to replicate this project? I think we can do this in minecraft. First we would need 3D data for navigations/spatial information. It might not be possible at first to also get a custom minecraft object detector model. So we can just set a constant bounding box and generate CLIP embeddings for that accordingly.

- Another thing that we can try in minecraft is that we can also get a list of objects like "tree" and "chicken" and then in order to search for a tree we just look for the query whose CLIP embedding had the cossim to "tree". Might be a good idea to do this search in the multimodal embedding space of MAGMA
