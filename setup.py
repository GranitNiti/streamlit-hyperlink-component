import setuptools

setuptools.setup(
    name="hyperlink_component",
    version="0.0.1",
    author="Granit Luzhnica",
    author_email="granit.luzhnica@gmail.com",
    description="A hyperlink component which allows to count the number of clicks",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.1",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
