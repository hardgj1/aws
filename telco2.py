import wikipedia
import nexmo
import click

@click.command()
@click.option('--cname')
@click.option('--key')
@click.option('--secret')
@click.option('--nfrom')
@click.option('--nto')
def api(cname, key, secret, nfrom, nto):
    ctext = wikipedia.summary(cname, sentences=1)
    client = nexmo.Client(key=key, secret=secret)
    result = client.send_message({
        'from': nfrom,
        'to': nto,
        'text': ctext,
    })
    print(f"Sent API message result: {result}")
    return result

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    api()