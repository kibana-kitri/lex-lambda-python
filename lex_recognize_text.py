# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime/client/recognize_text.html

import json
import boto3

client = boto3.client('lexv2-runtime')

def lambda_handler(event, context):
    input_text= "olá"
    
    # verificar no Redis cache se existe a intenção. Se não existir chama a api recognize_text

    response = client.recognize_text(
    botId='',
    botAliasId='',
    localeId='',
    sessionId='',  # A unique identifier for the session
    text=input_text
    )

    # Converte o dicionário Python em uma string JSON
    response_str = json.dumps(response)
    
    print(response_str)
    
    # U json.loads() com a string JSON
    data = json.loads(response_str)
    
    # Acessa a lista de interpretações
    interpretations = data["interpretations"]
    
    # Ordena as interpretações em ordem decrescente com base no score
    interpretations.sort(key=lambda x: x.get("nluConfidence", {}).get("score", 0), reverse=True)
    
    # Itera sobre as interpretações e imprime o score e o intent name
    for interpretation in interpretations:
        if "nluConfidence" in interpretation:
            score = interpretation["nluConfidence"]["score"]
        else:
            score = None
        intent_name = interpretation["intent"]["name"]
        print(f"Score: {score}, Intent Name: {intent_name}")
        
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(response)
    }
