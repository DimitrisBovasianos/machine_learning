# machine_learning

I extract all the searches that have been made from my website https://marketclaw.com.

Took the 2 firsts letters and the 2 last from the searched words and  I passed them to

a CSV file with ord() for each letter in order to get a number.

The code split the dataset in 2 pieces:

a 80% for training, and a 20% of testing later.

I create the dataset with pandas and i only use nonlinear algorithms for the training for the model.

Notes:

The most searched words have the better precision.

The code can be used to read words in search fields and suggests others.

Correcting spellings mistaces if didnt return the desirable results.

And finally in autocomplete(still working on that one)