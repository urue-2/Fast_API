''' using logistic regression \
classify whether the hand shaking model is normal \
based on 60 accelerations within 1 minute
'''

# data path
TRAIN_DATA_PATH = ""
TEST_DATA_PATH = ""



# dataset parameter
num_classes = 1  # 0-1 normal / abnormal
num_features = 60

# training parameters
learning_rate = 0.01
training_steps = 1000
batch_size = 256
display_step = 50

#Part1 prepare data
