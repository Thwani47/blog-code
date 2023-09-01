using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging.Abstractions;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Planning;

var configuration = new ConfigurationBuilder().SetBasePath(Directory.GetCurrentDirectory()).AddUserSecrets<Program>()
    .Build();
var apiKey = configuration.GetSection("OpenAI:APIKey").Value;

var loggerFactory = NullLoggerFactory.Instance;
var kernel = new KernelBuilder().WithLoggerFactory(loggerFactory)
    .WithOpenAITextCompletionService("text-davinci-003", apiKey!)
    .Build();


var pluginsDirectory = Path.Combine(Directory.GetCurrentDirectory(), "Plugins");
var writerPlugin = kernel.ImportSemanticSkillFromDirectory(pluginsDirectory, "WriterPlugin");

var textToSummarize =
    @"The Mars Perseverance Rover, a part of NASA's Mars Exploration Program, successfully landed on Mars on February 18, 2021. 
Its mission is to explore the Martian surface, collect samples, and study the planet's geology and climate. 
The rover is equipped with advanced instruments and cameras that allow scientists to analyze the terrain and search for signs of past microbial life. 
This mission represents a significant step towards our understanding of Mars and its potential to support life in the past or present.";

var summary = await writerPlugin["SummarizeText"].InvokeAsync(textToSummarize);
Console.WriteLine($"*****Summarized text:*****\n{summary}");

var poem = await writerPlugin["WritePoem"].InvokeAsync("Being a Software Developer");
Console.WriteLine($"*****Generated poem:*****\n{poem}");

var shortStory = await writerPlugin["GenerateStory"].InvokeAsync("The Lion and the Lamb");
Console.WriteLine($"*****Generated story:*****\n{shortStory}");

var translationContext = kernel.CreateNewContext();
translationContext.Variables["input"] = textToSummarize;
translationContext.Variables["target"] = "French";

var translatedText = await writerPlugin["Translate"].InvokeAsync(translationContext);
Console.WriteLine($"*****Translated text:*****\n{translatedText}");

var planner = new SequentialPlanner(kernel);
var ask = "Can you write a poem about being a software developer and translate it to German?";
var plan = await planner.CreatePlanAsync(ask);
var result = await plan.InvokeAsync();
Console.WriteLine(result);