using Xunit;

namespace Day5; 

public class Tests {
    [Fact]
    public void SilverTestCase() {
        const string input = @"";

        Assert.Equal(0, Silver.Run(input));
    }
    
    [Fact]
    public void GoldTestCase() {
        const string input = @"";

        Assert.Equal(1924, Gold.Run(input));
    }
}