using Xunit;

namespace Day19; 

public class Tests {
    [Fact]
    public void SilverTestCase() {
        const string input = @"0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: ""a""
5: ""b""

ababbb
bababa
abbbab
aaabbb
aaaabbb";
        
        Assert.Equal(2, Silver.Run(input));
    }

    
}