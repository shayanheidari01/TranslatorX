## TranslatorX

> A Python package for translation that uses Google translator and also supports asynchronous programming!

> Please star the GitHub repository to support me :)

### Simpale Example
```python
import asyncio
import TranslatorX

trans = TranslatorX.Translator()

async def main():
    print(trans.translator(text='hi', to_lang='fa'))

asyncio.run(main())
```

### Async Support
```python
import asyncio
import TranslatorX

trans = TranslatorX.AsyncTranslator()

async def main():
    print(await trans.translator(text='hi', to_lang='fa'))

asyncio.run(main())
```

### Install Package
```bash
pip3 install -U TranslatorX
```