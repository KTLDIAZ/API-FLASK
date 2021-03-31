from flask_restful import reqparse, Resource
from flask import request
import xgboost
import numpy as np
import json
import pandas as pd

class SumOfCards(Resource):

    def get(self):


        x = request.args.get("x")
        x = int(x)

        df = pd.read_csv('Data//blkjckhands.csv')
        
        
        del df['Unnamed: 0']
        del df['PlayerNo']
        del df['dlbustbeat']
        del df['plybustbeat']

        blkjck_map= {'nowin':0, 'Win':1}
        df['blkjck'] = df['blkjck'].map(blkjck_map)

        winloss_map= {'Push':1, 'Loss':2, 'Win':0}
        df['winloss'] = df['winloss'].map(winloss_map)

        
        length = (df.sumofcards==x).sum()

        win = ((df.sumofcards==x)  & (df.winloss==0)).sum()
        winPercentage = (win/length)*100

        loss = ((df.sumofcards==x)  & (df.winloss==2)).sum()
        lossPercentage = (loss/length)*100

        push = ((df.sumofcards==x)  & (df.winloss==1)).sum()
        pushPercentage = (push/length)*100

        return { 
            'Win_percentage': winPercentage,
            'Loss_percentage': lossPercentage,
            'Push_percentage': pushPercentage
         }


class PredictBlackjack(Resource):

    def get(self):
        
        df = pd.read_csv('Data//blkjckhands.csv')
        
        
        del df['Unnamed: 0']
        del df['PlayerNo']
        del df['dlbustbeat']
        del df['plybustbeat']

        blkjck_map= {'nowin':0, 'Win':1}
        df['blkjck'] = df['blkjck'].map(blkjck_map)

        winloss_map= {'Push':1, 'Loss':2, 'Win':0}
        df['winloss'] = df['winloss'].map(winloss_map)

        win = (df.blkjck==1).sum()

        win_blackjack = ((df.blkjck==1)& (df.winloss==0)).sum()
        win_blackjack = (win_blackjack/win)*100

        loss_blackjack = ((df.blkjck==1)& (df.winloss==2)).sum()
        loss_blackjack = (loss_blackjack/win)*100

        push_blackjack = ((df.blkjck==1)& (df.winloss==1)).sum()
        push_blackjack = (push_blackjack/win)*100

        return { 
            'win_blackjack_percentaje': win_blackjack,
            'loss_blackjack_percentaje': loss_blackjack,
            'push_blackjack_percentaje': push_blackjack
         }

class PredictWith2Cards(Resource):

    def get(self):

        card1 = request.args.get("card1")
        card1 = int(card1)

        card2 = request.args.get("card2")
        card2 = int(card1)

        df = pd.read_csv('Data//blkjckhands.csv')
            
            
        del df['Unnamed: 0']
        del df['PlayerNo']
        del df['dlbustbeat']
        del df['plybustbeat']

        blkjck_map= {'nowin':0, 'Win':1}
        df['blkjck'] = df['blkjck'].map(blkjck_map)

        winloss_map= {'Push':1, 'Loss':2, 'Win':0}
        df['winloss'] = df['winloss'].map(winloss_map)

        length = ((df.card1==card1) & (df.card2 ==card2) ).sum()


        win = ((df.card1==card1) & (df.card2 ==card2)  & (df.winloss==0)).sum()
        win = (win/length)*100

        loss = ((df.card1==card1) & (df.card2 ==card2)  & (df.winloss==2)).sum()
        loss = (loss/length)*100

        push = ((df.card1==card1) & (df.card2 ==card2)  & (df.winloss==1)).sum()
        push = (push/length)*100

        return { 
                    'win_percentaje': win,
                    'loss_percentaje': loss,
                    'push_percentaje': push
                }