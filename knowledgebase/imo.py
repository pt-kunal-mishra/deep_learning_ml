import os
import boto3
client=boto3.client('bedrock-agent-runtime',region_name='us-east-1',aws_access_key_id='AKIARSU7K4BC2SJER2N2',aws_secret_access_key='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')
kb_id="DDE1YCIJUN"
model_arn="arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-text-premier-v1:0"
def retrieval_generated(input,kb_id,model_arn):
    response = client.retrieve_and_generate(
        input={
            'text': input
        },
        retrieveAndGenerateConfiguration={
            'type':'KNOWLEDGE_BASE',
            'knowledgeBaseConfiguration':{
                'knowledgeBaseId': kb_id,
                'modelArn': model_arn
            }
           
        }
    )
    return response
response = retrieval_generated("Who is ian flemming?", kb_id, model_arn)
generated_text = response['output']['text']
print(generated_text)