import os
import boto3

client=boto3.client('bedrock-agent-runtime',
                    aws_access_key_id='AKIARSU7K4BCTATDUMFQ',
                    aws_secret_access_key='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')


kb_id="U9VVEW3HBZ"
model_arn="arn:aws:bedrock:us-east-1::foundation-model/mistral.mistral-large-2402-v1:0"

def retrieve_generated(input,kb_id,model_arn):
    response=client.retrieve_and_generate(
        input={
            'text':input
        },
        retrieveAndGenerateConfiguration={
            'type':'KNOWLEDGE_BASE',
            'knowledgeBaseConfiguration':{
                'knowledgeBaseId':kb_id,
                'modelArn':model_arn
            }
        }
    )

    return response

response=retrieve_generated('who is fleming',kb_id=kb_id,model_arn=model_arn)
generated_text=response['output']['text']

print(generated_text)


