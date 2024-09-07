
#include <stdio.h>
#include <math.h>

// Function to calculate shim
double shim(double a, double n, double x) {
    if (a == 0) return 0; // Avoid division by zero
    return sqrt(2 / a) * sin(n * M_PI * x / a);
}

// Function to plot the graph in ASCII
void plotGraph(double a, double n, double start, double end, int steps) {
    double x, y;
    int plotWidth = 60; // Width of the plot
    int i;

    for (i = 0; i <= steps; i++) {
        x = start + i * (end - start) / steps;
        y = shim(a, n, x);

        // Normalize the y value to fit in plot width
        int yPlot = (int)((y + 1) * (plotWidth - 1) / 2);

        // Print x and y
        printf("%6.2f ", x);
        for (int j = 0; j < plotWidth; j++) {
            if (j == yPlot)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
}

int main() {
    double a = 1.0; // Example value for a
    double n = 1.0; // Example value for n
    plotGraph(a, n, 0, 2 * M_PI, 100); // Plot from 0 to 2π
    return 0;
}
