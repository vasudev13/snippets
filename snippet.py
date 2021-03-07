%%capture
!git clone https://github.com/Atcold/pytorch-Deep-Learning.git
import os
os.chdir("/content/pytorch-Deep-Learning")


resnet18=torchvision.models.resnet18(pretrained=True)
resnet18.fc=nn.Linear(in_features=512,out_features=num_class)
