from flask import Flask, request, make_response
import re

app = Flask(__name__)

@app.route('/')
def home():
    response = "<h1>XSS challanges</h1>"
    for _ in range(8):
        data = f"<br><a href='/level{_}'>Level-{_}</a><br>"
        response+=data
    res = make_response(response+'<p>Trigger a alert(document.domain) as a proof of XSS</p><br><a href="https://github.com/skabdulhaq/xss-challange/blob/main/app.py">Source code</a>')
    return res


@app.route('/level0')
def level0():
    name = "Hacker"
    if request.args:
        name = request.args["name"]
        res = make_response(f"Hello {name}")
        res.set_cookie('password', 'flag{XSS_IS_BAD}')
        return res
    return f"Hello {name} welcome to level0<br>"


@app.route('/level1')
def level1():
    name = "Hacker"
    if request.args:
        name = request.args["name"]
        no_xss = re.sub('script', "", name)
        res = make_response(f"Hello {no_xss}")
        res.set_cookie('password', 'flag{XSS_regex_sanity_is_bad}')
        return res
    return f"Hello {name} welcome to level1"


@app.route('/level2')
def level2():
    name = "Hacker"
    if request.args:
        name = request.args["name"]
        no_xss = re.sub('<script>', "", name)
        no_xss = re.sub('</script>', "", no_xss)
        res = make_response(f"Hello {no_xss}")
        res.set_cookie('password', 'flag{xss_can_work_without_script_tag}')
        return res
    return f"Hello {name} welcome to level2"


@app.route('/level3')
def level3():
    name = "Hacker"
    if request.args:
        name = request.args["name"]
        no_xss = re.sub('<script>', "", name)
        no_xss = re.sub('</script>', "", no_xss)
        no_xss = re.sub('<img', "", no_xss)
        no_xss = re.sub('</img>', "", no_xss)
        res = make_response(f"Hello {no_xss}")
        res.set_cookie('password', 'flag{oops_blocking_image_cannot_Stop_xss}')
        return res
    return f"Hello {name} welcome to level3"


@app.route('/level4')
def level4():
    name = "Hacker"
    no_xss = 'https://media.tenor.com/nBt6RZkFJh8AAAAi/never-gonna.gif'
    if request.args:
        name = request.args["name"]
        no_xss = re.sub('/[<>]/g', "", name)
        res = make_response(
            f"Now you can add your images<br>Hello <img src='{no_xss}' />")
        res.set_cookie('password', 'flag{do_not_trust_profile_pics}')
        return res
    return f"Hello Hacker welcome to level4<br>Now you can add your images<br>Hello <img src='{no_xss}' />"


@app.route('/level5')
def level5():
    name = "Hacker"
    if request.args:
        name = request.args["name"]
        no_xss = re.sub('/[\(\`\)\\]/g', "", name)
        res = make_response(f"Now you can't use () <br>Hello {no_xss}")
        res.set_cookie('password', 'flag{you_can_not_stop_me_from_xss}')
        return res
    return f"Hello {name} welcome to level5"

@app.route('/level6')
def level6():
    name = "Hacker"
    if request.args:
        name = request.args["name"]
        no_xss = re.sub('/[A-Za-z0-9]/g', "", name)
        res = make_response(f"Now you can't use any letter or character <br>Hello <scripr>eval({no_xss})</script>")
        res.set_cookie('password', 'flag{no_character_filter_will_come_in_my_way}')
        return res
    return f"Hello {name} welcome to level6"

@app.route('/level7')
def level7():
    name = "Hacker"
    if request.args:
        name = request.args["name"]
        res = make_response(f"<script src='https://cdnjs.cloudflare.com/ajax/libs/dompurify/2.0.7/purify.min.js' integrity='sha256-iO9yO1Iy0P2hJNUeAvUQR2ielSsGJ4rOvK+EQUXxb6E=' crossorigin='anonymous'> /script>Now you can't use XSS <br>Hello <h1 id='name'></h1> <p>if you solve this send your payload to T!T4N#0717 in 1nf1n1ty server </p> <script>name.innerHTML = DOMPurify.sanitize({name})setTimeout(ok, 2000)</script>")
        res.set_cookie('password', 'flag{not_a_simple_bypass}')
        return res
    return f"Hello {name} welcome to level7"


if __name__ == "__main__":
    app.run("0.0.0.0", 3000, debug=True)
