import wikipedia
import nexmo
import click

def api(cname, key, secret, nfrom, nto):
    ctext = wikipedia.summary(cname, sentences=1)
    client = nexmo.Client(key=key, secret=secret)
    result = client.send_message({
        'from': nfrom,
        'to': nto,
        'text': ctext,
    })
    print(f"Sent message result: {result}")
    return result

@click.command()
@click.option('--cname')
@click.option('--key')
@click.option('--secret')
@click.option('--nfrom')
@click.option('--nto')
def callapi(cname, key, secret, nfrom, nto):
    print("About to call API")
    results = api(cname, key, secret, nfrom, nto)
    print(f"Sent API Call from CLI: {results}")
    
if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    callapi()


