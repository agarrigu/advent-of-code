package com.adventTools;

import java.util.*;
import java.util.stream.Stream;
import java.nio.file.Files;
import java.io.IOException;
import java.nio.file.Path;

public class ReadInput {

    public static String inputToString() {
        StringBuilder sb = new StringBuilder();
        Path path = Path.of("input.txt");
        Stream<String> stream = Files.lines(path);
        try (stream) {
            stream.forEach(s -> sb.append(s).append("\\n"));
        } catch (IOException ioe) {
            System.out.print("Could not stream input");
        }
        return sb.toString(); 
    }
}
