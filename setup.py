from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.0.1',
      description='code for cleaning folder',
      url='http://github.com/dummy_user/useful',
      author='Vesnani Fealds',
      author_email='vesnani.fields@example.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:clean']},
      )