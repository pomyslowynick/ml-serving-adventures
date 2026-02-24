## 24th Feb 2026

All of the dependencies used in this project are new to me.
Today I'm trying to make sense of FastAPI and how it works, then how we can expose an endpoint that accepts images to then predict whether it's a cat.

Feeling like I'm learning a ton doing all of this.

There must be some best practices when sending images for predictions over HTTP, gotta look them up.

Sending images wasn't too bad, but figuring out what format they should be in to be passed to torch is more difficult, will need more time to crack that one.

Debugger was handy here, it's pillow encoded jpeg, let's get something similar:

```
(Pdb) dataset["test"]["image"]
Column([<PIL.JpegImagePlugin.JpegImageFile image mode=RGB si
ze=640x480 at 0x7F198A7C9D10>])
(Pdb) dataset["test"]["image"][0]
<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x4
80 at 0x7F198A7C9D10>
(Pdb) 
```

I managed to get the predictions going! Model correctly classify both a cat and dog images I've tried, so simple yet so cool.

I'll use typer to improve the test client, might be really, really handy for testing eventually.

Pretty happy with todays progress, in just 1h30m I got a super basic serving server. It only gets more interesting from here.

I gotta do something about the model being loaded each time though, next time let's focus on improving the performance a good bit. Moving the model initialization to be global vars is my first attempt to improve it lol.
