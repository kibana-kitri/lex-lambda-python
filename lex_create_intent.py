# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/client/create_intent.html

import json
import boto3

def lambda_handler(event, context):

    # Crie um cliente para o serviço Amazon Lex Models V2
    lex_models_v2 = boto3.client('lexv2-models')
    
    # Chame a função create_intent para criar o novo intent
    # response = lex_models_v2.create_intent(intent_params)
    response = lex_models_v2.create_intent(
    intentName='',
    description='',
    botId='',
    botVersion='',
    localeId='',
    sampleUtterances=[
        {'utterance': 'olá'},
        {'utterance': 'sou eu'}
    ],
    intentClosingSetting={}
    )

    return {
        'statusCode': 200,
        'body': 'Ok'
    }
