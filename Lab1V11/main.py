import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import datetime as dt

blocks = [[2,1,4,1],[1,3,2,3],[2,4,1,2],[3,2,3,1]]

asyncMode = [

    # the first process

    dict(
        process=1,
        block=1,
        duration=dt.datetime.fromtimestamp(2).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(0).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=2,
        duration=dt.datetime.fromtimestamp(3).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(2).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=3,
        duration=dt.datetime.fromtimestamp(7).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(3).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=4,
        duration=dt.datetime.fromtimestamp(8).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(7).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # the second process

    dict(
        process=2,
        block=1,
        duration=dt.datetime.fromtimestamp(3).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(2).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=2,
        duration=dt.datetime.fromtimestamp(6).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(3).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=3,
        duration=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(7).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=4,
        duration=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # the third process

    dict(
        process=3,
        block=1,
        duration=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(3).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=2,
        duration=dt.datetime.fromtimestamp(10).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(6).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=3,
        duration=dt.datetime.fromtimestamp(11).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(10).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=4,
        duration=dt.datetime.fromtimestamp(14).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # the fourth process

    dict(
        process=4,
        block=1,
        duration=dt.datetime.fromtimestamp(8).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=2,
        duration=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(10).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=3,
        duration=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=4,
        duration=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S')
    ),
]

sync1Mode = [

    # the first process

    dict(
        process=1,
        block=1,
        duration=dt.datetime.fromtimestamp(2).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(0).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=2,
        duration=dt.datetime.fromtimestamp(3).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(2).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=3,
        duration=dt.datetime.fromtimestamp(7).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(3).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=4,
        duration=dt.datetime.fromtimestamp(8).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(7).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # the second process

    dict(
        process=2,
        block=1,
        duration=dt.datetime.fromtimestamp(4).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(3).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=2,
        duration=dt.datetime.fromtimestamp(7).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(4).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=3,
        duration=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(7).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=4,
        duration=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # the third process

    dict(
        process=3,
        block=1,
        duration=dt.datetime.fromtimestamp(7).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=2,
        duration=dt.datetime.fromtimestamp(11).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(7).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=3,
        duration=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(11).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=4,
        duration=dt.datetime.fromtimestamp(14).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # the fourth process

    dict(
        process=4,
        block=1,
        duration=dt.datetime.fromtimestamp(11).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(8).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=2,
        duration=dt.datetime.fromtimestamp(13).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(11).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=3,
        duration=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(13).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=4,
        duration=dt.datetime.fromtimestamp(17).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S')
    ),
]

sync2Mode = [

    # the first process

    dict(
        process=1,
        block=1,
        duration=dt.datetime.fromtimestamp(2).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(0).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=2,
        duration=dt.datetime.fromtimestamp(3).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(2).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=3,
        duration=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=4,
        duration=dt.datetime.fromtimestamp(11).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(10).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # the second process

    dict(
        process=2,
        block=1,
        duration=dt.datetime.fromtimestamp(3).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(2).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=2,
        duration=dt.datetime.fromtimestamp(6).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(3).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=3,
        duration=dt.datetime.fromtimestamp(11).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=4,
        duration=dt.datetime.fromtimestamp(14).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(11).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # the third process

    dict(
        process=3,
        block=1,
        duration=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(3).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=2,
        duration=dt.datetime.fromtimestamp(10).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(6).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=3,
        duration=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(11).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=4,
        duration=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(14).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # the fourth process

    dict(
        process=4,
        block=1,
        duration=dt.datetime.fromtimestamp(8).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=2,
        duration=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(10).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=3,
        duration=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=4,
        block=4,
        duration=dt.datetime.fromtimestamp(17).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S')
    ),
]

c_df = pd.DataFrame(asyncMode)
c_fig = px.timeline(c_df, x_start="start", x_end="duration", y="process", color="block")
c_fig.show()

c_df = pd.DataFrame(sync1Mode)
c_fig = px.timeline(c_df, x_start="start", x_end="duration", y="process", color="block")
c_fig.show()

c_df = pd.DataFrame(sync2Mode)
c_fig = px.timeline(c_df, x_start="start", x_end="duration", y="process", color="block")
c_fig.show()