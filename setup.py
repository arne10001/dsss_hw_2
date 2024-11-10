from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],  # List dependencies here if needed
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:main"  # Replace `main` with the function to run your quiz
        ]
    },
    author="Your Name",
    author_email="your-email@example.com",
    description="A simple math quiz game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/yourrepository",  # Replace with your repo URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
