from json import dumps
from bottle import Bottle, request, response
import dns.resolver

app = Bottle()

ids = [
    "A",
    "NS",
    "CNAME",
    "SOA",
    "MX",
    "TXT",
    "AAAA",
]


@app.get('/api')
def api():
    domain = request.query.get('domain')
    result = resolve(domain)
    print('result', result)
    return dict(data=result)
    

def resolve(domain: str):
    result = []
    for record in ids:
        try:
            answers = dns.resolver.query(domain, record)
            data = [{"record": record, "value": rdata.to_text()} for rdata in answers]
            for item in data:
                result.append(item)
        except Exception as e:
            print(e)
    return result
