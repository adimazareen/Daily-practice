import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend

import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot')
def plot():
    # Sample data
    x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
    y = np.sin(x)                 # Sine wave

    # Create the plot
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label='Sine Wave', color='blue')
    plt.title('Sine Wave Example')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()

    # Save the plot to a file
    plt.savefig('static/sine_wave.png')
    plt.close()  # Close the figure to prevent display

    return send_file('static/sine_wave.png')

if __name__ == '__main__':
    app.run(debug=True)
