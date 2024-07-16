from setuptools import setup

setup(name='PyFladesk-Pywebview',
      version='1.1',
      setup_requires=['setuptools-markdown'],
      long_description_markdown_filename='README.md',
      description='Create desktop application by using Flask and Pywebview',
      url="https://github.com/Willianjesusdasilva/PyFladesk-pywebview",
      author='Willian​',
      author_email='wjs140897@gmail.com',
      license='MIT',
      install_requires=[
          'flask',
          'pywebview',
          'werkzeug',
      ],
      packages=['pyfladesk-pywebview'],
      zip_safe=False,
      keywords = ['​GUI​', '​Flask​', 'pywebview'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3',
      ],
      python_requires='>=3',
      )