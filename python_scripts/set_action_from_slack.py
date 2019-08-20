import json

j = json.loads('slack_response')
logger.info(j['actions'][0]['value'])
