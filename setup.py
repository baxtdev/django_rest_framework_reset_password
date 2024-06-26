from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='django-rest-framework-reset-password',
  version='1.0.0',
  author='xwbxtdev',
  author_email='example@gmail.com',
  description='This module for auth regiters in django',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/baxtdev/django_rest_framework_reset_password',
  packages=find_packages(),
  install_requires=['django','rest_framework','markdown','django-rest-registration'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='files speedfiles ',
  project_urls={
    'GitHub': 'https://github.com/baxtdev'
  },
  python_requires='>=3.6'
)