from channels.consumer import SyncConsumer
import json
import pandas as pd

savedata = {}
class updateData(SyncConsumer):
    def websocket_connect(self,event):
        print("we are connected")
        self.send({
            'type': 'websocket.accept'
        })
    
    def websocket_disconnect(self,event):
        print("we are disconnected")
        self.send({'type': 'websocket.disconnect'})
    
    def websocket_receive(self,event):
        savedata.update(json.loads(event['text']))
        

        df = pd.DataFrame.from_dict(savedata, orient="index")

        df.to_csv("real_time_data.csv", mode='a')

        