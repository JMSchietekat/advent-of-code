open System
open System.IO

let sampleInput = "2021/day_05_input_sample.txt";
let challangeInput = "2021/day_05_input.txt";

let dataFromFile fileName =
    fileName
    |> File.ReadAllLines 
    |> Array.map (fun line -> line.Split(" -> "))
    |> Array.map (fun coordPair -> 
        [|
            coordPair.[0].Split(",") |> Array.map int;
            coordPair.[1].Split(",") |> Array.map int
        |])

let coordsToPoints (coordPair: int[][]) =
    let print message (coordPair: int[][]) = //(points: int[][]) =
        printfn "%s line, coords: %A, points: %A" 
            message coordPair

    let coord =
        if coordPair.[0] < coordPair.[1] then
            coordPair
        else
            [| coordPair.[1]; coordPair.[0] |]

    if coord.[0].[0] = coord.[1].[0] then
        print "Horizontal" coord [|for y in coord.[0].[1]..coord.[1].[1] -> [|coord.[0].[0];y|]|]
    else if coord.[0].[1] = coord.[1].[1] then
        print "Vertical" coord [|for x in coord.[0].[0]..coord.[1].[0] -> [|x;coord.[0].[1]|]|]
    else
        let m = 
            (coord.[1].[1] - coord.[0].[1]) / 
            (coord.[1].[0] - coord.[0].[0])

        let c = coord.[0].[1] - m * coord.[0].[0]

        print "Diagonal" coord [|for x in coord.[0].[0]..coord.[1].[0] -> [|x;m * x + c|]|]

let part1 fileName = 
    fileName
    |> dataFromFile
    |> Array.map (fun coordPair -> coordPair |> coordsToPoints)
    

part1 sampleInput
// part1 challangeInput 
