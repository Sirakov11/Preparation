from django.shortcuts import render


def calculator_view(request):
    result = None
    error = None

    if request.method == "POST":
        first_raw = request.POST.get("first", "").strip()
        second_raw = request.POST.get("second", "").strip()
        operation = request.POST.get("operation", "add")

        try:
            first = float(first_raw)
            second = float(second_raw)

            if operation == "add":
                result = first + second
            elif operation == "subtract":
                result = first - second
            elif operation == "multiply":
                result = first * second
            elif operation == "divide":
                if second == 0:
                    error = "Cannot divide by zero."
                else:
                    result = first / second
            else:
                error = "Unsupported operation."
        except ValueError:
            error = "Please enter valid numbers."

    return render(
        request,
        "calculator/index.html",
        {
            "result": result,
            "error": error,
        },
    )
