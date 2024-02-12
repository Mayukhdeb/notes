Craftassist is a cool project where the wuthors figured out a way to use natural language to communicate with a minecraft bot via chat. The even manage to give natural instructions to the robot to do certain tasks.

The first version of the bot had 3 main components:

1. Parsing incoming text into logical form ("action dictionary")
2. This parsed data is then interpreted by a dialogue object (not sure what that is).
3. This dialogue object thingy queries a memory module.

I think the memory module is the special part. It is a symbolic representation of the both's awareness of the world around it.

The bot has some low level actions like `MOVE`, `PUT BLOCK X` etc.

Given below is an example of a parsed human command:

```python
## input: "go to the blue house"
## output:
{
    "dialogue_type": "HUMAN_GIVE_COMMAND",
    "action": {
        "action_type": "MOVE",
        "location": {
            "location_type": "REFERENCE_OBJECT",
            "reference_object": {
                "has_colour": [0, [3, 3]],
                "has_name": [0, [4, 4]]
}}}}
```

(WIP)

<!-- 
steps I can take to better understand it:
1. make notes on how the memory works in craftassist. It might be the key to storing dynamic world knowledge.
2. understand how human input is parsed into low-level commands
3. Is it necessary for the bot to reply to the human in my case?


what can I build on top of this?
1. possibly better language parsing with out LLMs (check the craftassist dataset)
2. we can also have a visual interpreter/memory module. With MAGMA. (can store MAGMA embeddings of images)
3. Asking the bot questions about it's latest journey when it went into the woods to get some wood for his master.

What i want, is a natural language enabled skynet T1000 within minecraft :)

We can ask the bot to: "bring me this animal" and show it a picture of a chicken.
 -->