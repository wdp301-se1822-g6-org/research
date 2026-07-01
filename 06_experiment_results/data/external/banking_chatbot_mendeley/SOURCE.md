# Source - Banking Chatbot Service Quality Survey

Dataset: Data on Banking Chatbot Service Quality

Repository: Mendeley Data

DOI: 10.17632/jsvbvgzkf8.4

URL: https://data.mendeley.com/datasets/jsvbvgzkf8/4

Published: 2 April 2024, Version 4

Contributor: Poornima Purushotham

License: CC BY 4.0

## Why this dataset is used

This dataset is used as the external, verified survey source for Experiment E2. It contains survey responses from banking chatbot users and includes constructs that match the paper's customer-service loyalty model:

- AI chatbot service-quality dimensions
- personalization
- customer value
- customer satisfaction
- customer trust
- customer loyalty

The original repository description states that a structured questionnaire was distributed to Indian banking chatbot users in Bangalore and that all items used a five-point Likert scale. The raw dataset represents missing or incomplete answers with `0`.

## Files saved locally

- `banking_chatbot_raw.csv`: raw survey responses downloaded from Mendeley Data.
- `final_code.xlsx`: codebook / variable descriptions from Mendeley Data.
- `questionnaire.pdf`: original questionnaire file from Mendeley Data.
- `irb_clearance.pdf`: ethics / IRB clearance file from Mendeley Data.

## Analysis notes

The questionnaire scale is coded as:

- 1 = Strongly Agree
- 2 = Agree
- 3 = Neither agree nor disagree
- 4 = Disagree
- 5 = Strongly disagree

To make higher scores consistently represent more positive perceptions, the E2 external analysis script reverse-codes Likert items as `6 - value` after converting `0` to missing values.
