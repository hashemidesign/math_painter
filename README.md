# Math Painter Drawing Program

This Drawing Program is a simple tool for creating customizable drawings on a canvas and saving them as PNG images.

## Features

- Create a canvas of custom width, height, and color.
- Draw rectangles and squares on the canvas with custom positions, sizes, and colors.
- Save the drawing as a PNG image file.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/drawing_program.git
    cd drawing_program
    ```

2. Create a virtual environment and activate it:
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
```bash
python main.py
```


## File Structure
```plaintext
math_painter/
│
├── models/
│   ├── canvas.py           # Contains the Canvas class
│   ├── rectangle.py        # Contains the Rectangle class
│   └── square.py           # Contains the Square class
├── output/
│   └── canvas.png          # Generated PNG image
├── main.py                 # Main script to run the application
└── requirements.txt        # List of dependencies
```

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add some new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please open an issue or contact [m.hashemi.code@gmail.com](mailto:m.hashemi.code@gmail.com).