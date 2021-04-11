html = """<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>НАЧАЛО РАБОТЫ С BRACKETS</title>
    <meta name="description" content="Интерактивное руководство по началу работы в Brackets.">
    <link rel="stylesheet" href="css/tv_css.css">
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .image {
            position: relative;
            width: 100%;
        }

        .image img {
            width: 100%;
            object-fit: cover;
        }

        h2 {
            position: absolute;
            bottom: 50px;
            left: 0;
            width: 100%;
        }

        h2 span {
            color: white;
            font: bold 3vw/4.3vw Helvetica, Sans-Serif;
            letter-spacing: -1px;
            background: rgb(0, 121, 242);

            /* на случай, если следующая строка не сработает */
            padding: 10px;

        }

        h2 span.spacer {
            padding: 0 5px;
        }

    </style>
</head>

<div class="image">
    <img src="{{ img_url }}" alt="" />
    <h2>
        <span>
            {% for name in names %}
                {{ name }}
                <span class="spacer"></span>
                <br/>
                <span class="spacer"></span>
            {% endfor %}
            {{ second }}
            {% if third != '' %}
                <span class="spacer"></span>
                <br/>
                <span class="spacer"></span>
                {{ third }}
            {% endif %}
            </span>
    </h2>
</div>

</html>
"""
