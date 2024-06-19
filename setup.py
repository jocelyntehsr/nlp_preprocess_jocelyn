import setuptools

with open('README.md','r') as file:
    long_description = file.read()

setuptools.setup(
    name = 'nlp_preprocess_jocelyn',
    version = '0.0.2',
    author = 'Jocelyn Teh',
    description= 'This is Preprocessing Package NLP',
    long_description= long_description,
    long_description_content_type= 'text/markdown',
    packages= setuptools.find_packages(),
    classifiers= [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires = '>=3.5'
)