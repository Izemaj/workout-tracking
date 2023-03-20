<!DOCTYPE html>
<html>
  <head>
    <title>Workout Tracker</title>
  </head>
  <body>
    <h1>Workout Tracker</h1>
    <p>
      This Python script tracks your workouts by using the Nutritionix API to get
      exercise data based on your input, and then sending the workout information
      to a Google Sheets document using the Sheety API.
    </p>
    <h2>Prerequisites</h2>
    <ul>
      <li>Python 3 installed on your machine</li>
      <li>API credentials for Nutritionix and Sheety</li>
      <li>A Google Sheets document created in your Sheety account</li>
    </ul>
    <h2>Installation</h2>
    <ol>
      <li>Clone this repository on your local machine</li>
      <li>
        Install the required Python packages by running the following command in your terminal:
        <pre>pip install requests</pre>
      </li>
      <li>
        Export your API credentials as environment variables in your terminal, like this:
        <pre>
export TOKEN=&lt;your-sheety-api-token&gt;
export NUTRITION_APP_ID=&lt;your-nutritionix-app-id&gt;
export NUTRITION_API_KEY=&lt;your-nutritionix-api-key&gt;
        </pre>
      </li>
      <li>
        Run the script by running the following command in your terminal:
        <pre>python workout_tracker.py</pre>
      </li>
    </ol>
    <h2>Usage</h2>
    <ol>
      <li>The script will ask you to enter the exercises you did in natural language format. For example, "I ran for 30 minutes and did 20 pushups".</li>
      <li>The script will use the Nutritionix API to get the exercise data and calculate the calories burned.</li>
      <li>The script will then send the workout information to your Google Sheets document using the Sheety API.</li>
    </ol>
    <h2>Output</h2>
    <p>
      The script will output the workout information in the following format:
    </p>
    <pre>
    Exercise: &lt;exercise_name&gt;
    Duration: &lt;duration_in_minutes&gt; minutes
    Calories Burned: &lt;calories_burned&gt;
    </pre>
    <p>
      The information will also be sent to your Google Sheets document using the Sheety API.
    </p>
  </body>
</html>
