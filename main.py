from flask import Flask, render_template
import random

app = Flask(__name__)

#default page when
@app.route('/')
def home():
    return 'Welcome to Monte Carlo Pi Estimation!'

@app.route('/pi_estimate/<int:total_points>')
def estimate_pi(total_points):
    points_inside = 0

    for _ in range(total_points):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 0.5**2:
            points_inside += 1

    estimated_pi = 4 * (points_inside / total_points)
    print(points_inside, total_points, estimated_pi)
    return render_template('pi_estimate.html', total_points=total_points, estimated_pi=estimated_pi)

if __name__ == '__main__':
    app.run(debug=True)