from setuptools import setup

setup(
        name = 'citnetparser',
        version = '1.0.0',
        description = 'A parsing utility from CitNetExplorer output to a GML file.',
        author = 'Jan Tschopp',
        author_email = 'tschoppj@ethz.ch',
        license = 'MIT',
        
        packages = [
            'citnetparser'
        ],

        entry_points = {
            'console_scripts': [
                'citnetparser = citnetparser.__main__:main'
            ]
        }
)
