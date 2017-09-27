"""Define flags and provide a function to get options from the flags.
"""

import tensorflow as tf

f = tf.app.flags
f.DEFINE_integer("max_ctx_length", 600,
        "Max passage length to keep. Content longer will be trimmed.")
f.DEFINE_integer("max_qst_length", 30,
        "Max question length to keep. Content longer will be trimmed.")
f.DEFINE_string("model_type", "match_lstm", "Type of model to train.")
f.DEFINE_boolean("debug", True, "Whether or not debugging is on.")
f.DEFINE_string("experiment_name", "logistic_regression",
        "Name of the experiment being run; different experiments will be " +
        "saved and loaded from different model files and can use different " +
        "model hyperparameters")
f.DEFINE_string("checkpoint_dir", "checkpoint",
        "Directory to save model weights and metadata.")
f.DEFINE_float("learning_rate", 1e-3, "Initial learning rate.")
f.DEFINE_float("min_learning_rate", 1e-5,
        "Minimum learning rate, even after decay.")
f.DEFINE_float("learning_rate_decay", 0.9,
        "Learning rate to apply continuously over each epoch.")
f.DEFINE_string("data_dir", "data",
        "Directory with word embeddings, vocab, and training/dev data.")
f.DEFINE_string("log_dir", "log", "Directory to log training summaries. " +
        "These summaries can be monitored with tensorboard.")
f.DEFINE_string("clear_logs_before_training", True,
        "Whether to clear the log directory before starting training.")
f.DEFINE_integer("log_every", 10, "Frequency to log loss and gradients.")
f.DEFINE_string("log_loss", True, "Whether to log loss summaries.")
f.DEFINE_string("log_gradients", True, "Whether to log gradient summaries.")
f.DEFINE_string("log_exact_match", True, "Whether to log exact match scores.")
f.DEFINE_string("log_f1_score", True, "Whether to log f1 scores.")
f.DEFINE_string("log_valid_every", 100, "Frequency (in iterations) to log " +
        "loss & gradients for the validation data set.")
f.DEFINE_integer("compute_accuracy_every", 200, "Frequency (in iterations) " +
        "to compute exact matach and f1 scores on the training and " +
        "validation data sets.")
f.DEFINE_integer("save_every", 400, "Frequency (in iterations) to save the "
        "model.")
f.DEFINE_boolean("use_s3", False,
        "Whether to use AWS S3 storage to save model checkpoints. " +
        "Checkpoints will be saved according to the experiment name and " +
        "model type.")
f.DEFINE_string("s3_bucket_name", "zippy-machine-learning",
        "The AWS S3 bucket to save models to.")
f.DEFINE_string("s3_data_folder_name", "data", "Folder within the S3 bucket " +
        "to store train/dev data and word vector indices. Only applies if " +
        "s3 storage is enabled. Using this makes it faster to start up "
        "training on another instance, rather than using SCP to upload " +
        "files and then unzip them on the EC2 instance.")
f.DEFINE_integer("num_gpus", 0, "Number of GPUs available for training. " +
        "Use 0 for CPU-only training")
f.DEFINE_integer("batch_size", 20, "Training batch size. If using GPUs, " +
        "then this will be the same for each GPU.")
f.DEFINE_integer("epochs", 10, "Number of epochs to train")
f.DEFINE_integer("num_evaluation_samples", 200, "Number of samples of the " +
        "datasets to take for partial exact match and f1 score evaluations." +
        "This is done since it can take a while to evaluate the model on the" +
        "whole dataset")
f.DEFINE_integer("rnn_size", 50, "The dimension of rnn cells.")
f.DEFINE_integer("num_rnn_layers", 1, "The number of rnn layers to use in " +
        "a single multi-rnn cell.")
f.DEFINE_float("dropout", 0.2, "The amount of dropout to use.")

def get_options_from_flags():
    flags = tf.app.flags.FLAGS
    if flags.debug:
        flags.num_evaluation_samples = 10
        flags.batch_size = 4
        flags.max_ctx_length = 10
        flags.max_qst_length = 8
        flags.clear_logs_before_training = True
        flags.log_loss = True
        flags.log_gradients = True
        flags.log_exact_match = True
        flags.log_f1_score = True
        flags.log_every = 1
        flags.log_valid_every = 4
        flags.compute_accuracy_every = 4
        flags.save_every = 4
    return flags