from torch import nn



class AutoEncoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(
                nn.Linear(8420, 2048),
                nn.BatchNorm1d(2048),
                nn.ReLU(),
                nn.Linear(2048,1024),
                nn.BatchNorm1d(1024),
                nn.ReLU(),
                nn.Linear(1024, 256),
                nn.BatchNorm1d(256),
                nn.ReLU(),
                nn.Linear(256, 64),
        )
        self.decoder = nn.Sequential(
                nn.Linear(64,256),
                nn.BatchNorm1d(256),
                nn.ReLU(),
                nn.Linear(256,1024),
                nn.BatchNorm1d(1024),
                nn.ReLU(),
                nn.Linear(1024,2048),
                nn.BatchNorm1d(2048),
                nn.ReLU(),
                nn.Linear(2048,8420),
        )

    def forward(self, x):
        code = self.encoder(x)
        right_out = self.decoder(code)
        return code,right_out
