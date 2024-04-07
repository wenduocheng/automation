import numpy as np
import torch
import torch.nn as nn

import torch.nn.functional as F



class DeepSEA_Original(nn.Module):
    def __init__(self, ):
        super(DeepSEA_Original, self).__init__()
        self.Conv1 = nn.Conv1d(in_channels=4, out_channels=320, kernel_size=8)
        self.Conv2 = nn.Conv1d(in_channels=320, out_channels=480, kernel_size=8)
        self.Conv3 = nn.Conv1d(in_channels=480, out_channels=960, kernel_size=8)
        self.Maxpool = nn.MaxPool1d(kernel_size=4, stride=4)
        self.Drop1 = nn.Dropout(p=0.2)
        self.Drop2 = nn.Dropout(p=0.5)
        self.flatten = nn.Flatten()
        self.Linear1 = nn.Linear(53*960, 925) 
        self.Linear2 = nn.Linear(925, 36)
        
    def forward(self, input):
        x = self.Conv1(input)
        x = F.relu(x)
        x = self.Maxpool(x)
        x = self.Drop1(x)
        x = self.Conv2(x)
        x = F.relu(x)
        x = self.Maxpool(x)
        x = self.Drop1(x)
        x = self.Conv3(x)
        x = F.relu(x)
        x = self.Drop2(x)
        x = self.flatten(x)
        x = self.Linear1(x)
        x = F.relu(x)
        x = self.Linear2(x)
  
        return x
    
    
 
def get_model():
    return DeepSEA_Original()
    
    
    
    



