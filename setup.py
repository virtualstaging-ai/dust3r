from setuptools import setup, find_packages

setup(
    name='dust3r',
    version='0.1',
    packages=find_packages(),
    description='Code for dust3r.',
    long_description=open('../README.md').read(),
    long_description_content_type='text/markdown',
    author='Michal Stary',
    author_email='michal@virtualstagingai.app',
    url='https://virtualstagingai.app/',
    classifiers=[],
    keywords='',
    install_requires=[

        # 'numpy', 
        # 'pandas', 
        # 'diffusers', 
        # 'datasets',
        # 'torch', 
        # 'pillow==9.5.0', 
        # 'matplotlib', 
        # 'prettytable',
        # also needs vsai_utils; install with your own github key
    ],
    python_requires='~=3.11',
)