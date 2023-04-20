+++
title = "THINGS: a multimodal dataset for investigating object representations in thehuman brain"
date = "2023-04-04"
author = "Mayukh Deb"
tags = ["paper"]
+++

It's actually a collection of 3 datasets. All of which can be found [here](https://openneuro.org/datasets/ds004212/versions/2.0.0). The images used can be found [here](https://things-initiative.org/).

The 3 datasets are:
1. FMRI scans from 3 participants. 8740 images.
2. MEG scans. 4 participants. 22k images.
3. 12k participants. 4.7 million similarity judgements.

The 2 main datasets I'm interested in are the MEG scans and the similarity judgements. For the MEG scans, we can use [these scripts](https://github.com/ViCCo-Group/THINGS-data/tree/main/MEG) as boilerplate.

For now lets stick to MEG as planned.

Notes on MEG data collection:
- Each session consisted of 10 runs (~5 min each). 
- In each run, 185–186 object images were presented, as well as 20 test and 20 catch images
- Stimuli were presented for 500ms
- 225–226 trials per run, 2,254 trials per session
- 27,048 trials per participant
- Stimulus presentation was done with Psychtoolbox

Metadata for a single MEG run for session 1 run 9:
```python
{
    "TaskName": "main",
    "Manufacturer": "CTF",
    "PowerLineFrequency": 60,
    "SamplingFrequency": 1200.0,
    "SoftwareFilters": "n/a",
    "RecordingDuration": 347.99916666666667,
    "RecordingType": "continuous",
    "DewarPosition": "n/a",
    "DigitizedLandmarks": false,
    "DigitizedHeadPoints": false,
    "MEGChannelCount": 272,
    "MEGREFChannelCount": 28,
    "EEGChannelCount": 0,
    "EOGChannelCount": 0,
    "ECGChannelCount":+ 0,
    "EMGChannelCount": 0,
    "MiscChannelCount": 10,
    "TriggerChannelCount": 0
}
```

I think `"MEGChannelCount": 272` refers to the fact that we have 272 channels. So if we average along the time dimension, then for each instance, we get a tensor of shape `272`.

Files like [these](https://openneuro.org/datasets/ds004212/versions/2.0.0/file-display/sub-BIGMEG1:ses-11:meg:sub-BIGMEG1_ses-11_task-main_run-01_events.tsv) contain the index of the image used (most probably it's that)

**Open questions:**
1. what is `TRIAL_TYPE`? (values: `['exp', 'test', 'catch'...]`)