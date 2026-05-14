"""
===========================================================
MORSE LOVER - WEB DASHBOARD
===========================================================

Requirements:
    pip install flask

Run:
    python morse_dashboard.py

Open Browser:
    http://127.0.0.1:5000
===========================================================
"""

from flask import Flask, render_template_string, request , send_file
from morse_backend import MorseCodeTranslator

app = Flask(__name__)

translator = MorseCodeTranslator()

# ============================================================
# HTML TEMPLATE
# ============================================================

HTML_TEMPLATE = """

<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Morse</title>

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:Arial, sans-serif;
        }

        body{
            background:#0f172a;
            color:white;
            min-height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            padding:20px;
        }

        .container{
            width:100%;
            max-width:1000px;
            background:#111827;
            padding:30px;
            border-radius:20px;
            box-shadow:0px 0px 30px rgba(0,0,0,0.5);
        }

        h1{
            text-align:center;
            margin-bottom:10px;
            font-size:3rem;
        }

        .subtitle{
            text-align:center;
            margin-bottom:30px;
            color:#94a3b8;
        }

        textarea{
            width:100%;
            min-height:180px;
            padding:20px;
            border:none;
            border-radius:15px;
            resize:vertical;
            font-size:16px;
            margin-bottom:20px;
            background:#1e293b;
            color:white;
        }

        textarea:focus{
            outline:none;
        }

        .buttons{
            display:flex;
            gap:15px;
            flex-wrap:wrap;
            margin-bottom:20px;
        }

        button{
            flex:1;
            min-width:200px;
            padding:15px;
            border:none;
            border-radius:12px;
            cursor:pointer;
            font-size:16px;
            font-weight:bold;
            transition:0.3s;
        }

        .encode{
            background:#22c55e;
            color:white;
        }

        .decode{
            background:#3b82f6;
            color:white;
        }

        .clear{
            background:#ef4444;
            color:white;
        }

        button:hover{
            transform:translateY(-2px);
            opacity:0.9;
        }

        .output-box{
            background:#1e293b;
            padding:20px;
            border-radius:15px;
            min-height:150px;
            white-space:pre-wrap;
            word-wrap:break-word;
            line-height:1.6;
        }

        .footer{
            margin-top:25px;
            text-align:center;
            color:#94a3b8;
        }

        @media(max-width:700px){

            h1{
                font-size:2rem;
            }

            button{
                min-width:100%;
            }
        }

    </style>

</head>

<body>

    <div class="container">

        <h1>⚡Morse⚡</h1>

        <p class="subtitle">
            Encode & Decode Any Text Into Morse Code
        </p>

        <form method="POST">

            <textarea
                name="user_input"
                placeholder="Type text or Morse code here..."
            >{{ user_input }}</textarea>

            <div class="buttons">

                <button class="encode" name="action" value="encode">
                    Convert Text → Morse
                </button>

                <button class="decode" name="action" value="decode">
                    Convert Morse → Text
                </button>

                <button class="clear" name="action" value="clear">
                    Clear
                </button>

            </div>

        </form>

        <div class="output-box">
{{ output }}
        </div>
        {% if output %}
<div style="margin-top:20px;">

    <audio controls style="width:100%;">
        <source src="/audio" type="audio/wav">
    </audio>

</div>
{% endif %}

        <div class="footer">
            Built with Python + Flask ❤️
        </div>

    </div>

</body>

</html>

"""

# ============================================================
# ROUTE
# ============================================================

@app.route("/", methods=["GET", "POST"])
def home():

    output = ""
    user_input = ""

    if request.method == "POST":

        action = request.form.get("action")
        user_input = request.form.get("user_input")

        if action == "encode":
            output = translator.text_to_morse(user_input)
            translator.generate_morse_audio(output)

        elif action == "decode":
            output = translator.morse_to_text(user_input)

        elif action == "clear":
            user_input = ""
            output = ""

    return render_template_string(
        HTML_TEMPLATE,
        output=output,
        user_input=user_input
    )

@app.route("/audio")
def audio():

    return send_file(
        "static/morse_audio.wav",
        mimetype="audio/wav"
    )


# ============================================================
# RUN SERVER
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )