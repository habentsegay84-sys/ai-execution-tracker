# File: worst_nn.py - CREATE THIS TODAY
import random

# TERRIBLE variable names
a = [1, 2, 3]  # Not even weights, just random numbers
b = "neural"   # Wrong type entirely
c = False      # Useless boolean

def train(x, y):
    # This function makes the model WORSE
    global a
    a = [0, 0, 0]  # Destroy any learning
    return -999  # Negative progress on purpose

def predict(x):
    # Always wrong predictions
    if random.random() > 0.5:
        return "cat"  # Should be number
    else:
        return 42.0  # Arbitrary constant

# INTENTIONAL ERRORS:
# 1. No actual neural network
# 2. Mixed return types
# 3. Training destroys weights
# 4. No loss function
# 5. No layers, no activation
# 6. Global variables (bad practice)
# 7. Random predictions
# 8. Wrong parameter types

print("WORST AI MODEL READY")
print("Training... Progress:", train([1,2,3], 1))
print("Prediction for 5:", predict(5))
