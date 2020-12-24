import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="riscv_assembler",
    version="1.0.2",
    author="Kaya Çelebi",
    author_email="kayacelebi17@gmail.com",
    description="RISC-V assembler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kcelebi/riscv_assembler",
    packages=setuptools.find_packages(),
    package_dir={'riscv_assembler':'.'},
    package_data={'riscv_assembler':['data/*.dat']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)