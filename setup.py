from setuptools import setup, find_packages
import select2

setup(
    name='twentytab-select2',
    version=select2.__version__,
    description='A django app to customize your admin interface with icons for applications and models and other stuffs',
    author='20tab S.r.l.',
    author_email='info@20tab.com',
    url='https://github.com/20tab/twentytab-select2',
    license='MIT License',
    install_requires=[
        'Django >=1.6',
        'django-appconf>=0.6',
    ],
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.html', '*.css', '*.js', '*.gif', '*.png', ],
}
)
