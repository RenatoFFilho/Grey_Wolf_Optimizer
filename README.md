# Grey Wolf Optimizer (GWO) Python Implementation

![Grey Wolf](wolf.jpg)

Welcome to the Grey Wolf Optimizer (GWO) Python Implementation repository! This project provides a versatile and efficient implementation of the Grey Wolf optimization algorithm for solving complex optimization problems.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

## About

The Grey Wolf Optimizer is a nature-inspired optimization algorithm based on the hunting behavior of grey wolves. It is particularly effective for solving a wide range of optimization problems across various domains. This implementation aims to provide an easy-to-use yet powerful tool for researchers and practitioners.

## Features

- Easy integration into your optimization projects.
- Support for single-dimensional and multi-dimensional optimization problems.
- Efficient alpha, beta, and delta calculation for global exploration.
- Flexibility to define custom objective functions and problem constraints.

## Installation

To use the Grey Wolf Optimizer in your project, simply clone this repository:

```bash
git clone https://github.com/RenatoFFilho/Grey_Wolf_Optimizer.git
```

## Usage

1. Import the `Grey_Wolf_Optimizer` class into your Python project.
2. Define your objective function to be minimized.
3. Configure optimization parameters and constraints.
4. Run the optimization using the `.run()` method of the `Grey_Wolf_Optimizer` class.

```python
from gwo import Grey_Wolf_Optimizer

# Define your objective function
def objective_function(x):
    # Your objective function logic here

# Configure optimization parameters
parameters = {
    'funcao': objective_function,
    'n_dim': 2,  # Number of dimensions
    'lim': [(-10, 10), (-5, 5)],  # Search space limits for each dimension
    'max_iter': 100,
}

# Create the optimizer instance
optimizer = Grey_Wolf_Optimizer(parameters)

# Run the optimization
best_solution, best_fitness = optimizer.run()

print(f"Best solution: {best_solution}")
print(f"Best fitness value: {best_fitness}")
```
## Examples

Explore the [`examples`](examples/) directory for detailed usage examples and sample problems.

To run the provided examples, follow these steps:

1. Navigate to the `examples` directory: `cd examples`.
2. Choose an example file.
3. Run the chosen example using Python.

## Contributing

Contributions are welcome! If you find any issues or have improvements to suggest, please feel free to submit a pull request following our [contribution guidelines](CONTRIBUTING.md).

We appreciate your efforts to make this project better and more useful for the community. Whether it's bug fixes, feature enhancements, or documentation improvements, your contributions are highly valued.

Before contributing, make sure to:

1. Fork the repository.
2. Create a new branch for your changes: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m "Add your message here"`.
4. Push your changes to your fork: `git push origin feature/your-feature-name`.
5. Open a pull request and provide a clear description of your changes.

Thank you for contributing to the Grey Wolf Optimizer Python Implementation!

## Contact

If you have any questions, suggestions, or would like to collaborate, please reach out to me via [email](mailto:renato.luiz@engenharia.ufjf.br) or connect with me on [LinkedIn](https://www.linkedin.com/in/renato-faraco/).

## License

This project is licensed under the [GNU General Public License (GPL)](LICENSE).

---

Feel free to adapt, extend, and utilize this Grey Wolf Optimizer implementation to enhance your optimization tasks. Happy optimizing!


