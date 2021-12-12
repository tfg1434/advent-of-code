using Xunit;

namespace Day12; 

public class Tests {
    [Fact]
    public void SilverTestCase() {
        const string input = @"start-A
start-b
A-c
A-b
b-d
A-end
b-end";

        Assert.Equal(10, Silver.Run(input));
    }
    
    [Fact]
    public void SilverTestCase2() {
        const string input = @"dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc";

        Assert.Equal(19, Silver.Run(input));
    }
    
    [Fact]
    public void GoldTestCase() {
        const string input = @"start-A
start-b
A-c
A-b
b-d
A-end
b-end";

        Assert.Equal(36, Gold.Run(input));
    }
}