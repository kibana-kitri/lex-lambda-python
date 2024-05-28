# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models/client/update_intent.html

import json
import boto3

def lambda_handler(event, context):
    
    # Crie um cliente para o serviço Amazon Lex Models V2
    lex_models_v2 = boto3.client('lexv2-models')

    # Chamar a API para atualizar a intenção
    
    response = lex_models_v2.update_intent(
    botId='',
    botVersion='',
    localeId='',
    intentId='',
    intentName='',
    description='',
    sampleUtterances= [
        {'utterance': 'olá'},
        {'utterance': 'sou eu'}
    ]
    )

    return {
        'statusCode': 200,
        'body': 'Ok'
    }
