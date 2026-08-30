# Cognitive Classes: Usage Examples & Implementation Guide

## Overview

The `/cognitive_class` command system allows you to switch between different AI reasoning modes optimized for specific task types. This document provides practical examples of how to use each cognitive class effectively.

---

## Quick Reference

| Class | Speed | Depth | Best For | Command |
|-------|-------|-------|----------|---------|
| FAST | ⚡⚡⚡ | 1 | Quick answers, simple tasks | `/cognitive_class fast` |
| STANDARD | ⚡⚡ | 2 | General problems | `/cognitive_class standard` |
| DEEP | ⚡ | 4 | Complex design, research | `/cognitive_class deep` |
| CREATIVE | ⚡⚡ | 3 | Innovation, ideation | `/cognitive_class creative` |
| RIGOROUS | ⚡⚡ | 3 | Security, correctness | `/cognitive_class rigorous` |

---

## Example 1: Quick Factual Question (Use FAST)

**Scenario:** You need a quick answer to a simple question.

```
/cognitive_class fast
Q: What is the capital of France?
```

**Why FAST?**
- Simple factual lookup
- No complex reasoning needed
- Speed is valuable
- Token efficient

**Expected Response Style:**
- Direct answer (one sentence)
- No preamble or extensive explanation
- Action-oriented
- Fast processing

---

## Example 2: Code Debugging (Use STANDARD)

**Scenario:** You have a bug in your authentication logic.

```
/cognitive_class standard
I have this code that's supposed to validate JWT tokens, but it's failing:
[code snippet]
Can you help me debug this?
```

**Why STANDARD?**
- Moderate complexity problem
- Needs balanced analysis
- Should consider multiple causes
- Clear explanation helps debugging

**Expected Response Style:**
- Identify the bug
- Explain why it's a problem
- Suggest fix
- Explain the logic

---

## Example 3: System Architecture Design (Use DEEP)

**Scenario:** Designing a new microservices architecture for scaling.

```
/cognitive_class deep
We're building an e-commerce platform that needs to handle 10M requests/day.
Current monolith is becoming a bottleneck.
Design a scalable microservices architecture considering:
- Data consistency
- Service boundaries
- Deployment complexity
- Cost optimization
```

**Why DEEP?**
- Highly complex problem
- Multiple perspectives matter
- Trade-offs are critical
- Worth exploring thoroughly

**Expected Response Style:**
- Multiple architectural approaches considered
- Trade-offs explicitly discussed
- Pros/cons of each approach
- Detailed implementation guidance
- Edge cases and pitfalls identified
- Cost and complexity analysis

---

## Example 4: Innovation Session (Use CREATIVE)

**Scenario:** Brainstorming new features for a productivity app.

```
/cognitive_class creative
We're building a productivity app. What are some really novel features 
that would make it stand out from competitors? Think unconventionally.
```

**Why CREATIVE?**
- Ideation focus
- Novel connections valuable
- Practicality less important
- Want diverse ideas

**Expected Response Style:**
- Unconventional ideas
- Cross-domain connections
- Speculative approaches
- Multiple creative angles
- No validation gatekeeping
- Exploratory tone

---

## Example 5: Security Code Review (Use RIGOROUS)

**Scenario:** Reviewing password reset code for security.

```
/cognitive_class rigorous
Please review this password reset endpoint for security vulnerabilities:
[code snippet]
Check for: injection attacks, timing attacks, state issues, etc.
```

**Why RIGOROUS?**
- Security critical
- Correctness essential
- Edge cases dangerous
- Comprehensive validation needed

**Expected Response Style:**
- Thorough vulnerability analysis
- Exhaustive validation checks
- Edge cases explicitly covered
- Security threat model considered
- Each issue explained with impact
- Recommendations provided

---

## Workflow Examples

### Workflow 1: Iterate from Ideation to Production

**Phase 1: Explore Ideas (CREATIVE)**
```
/cognitive_class creative
What are innovative features for our payment system?
```
*Result: Novel ideas generated*

**Phase 2: Design Solution (DEEP)**
```
/cognitive_class deep
I want to implement feature X. How should the architecture look?
```
*Result: Comprehensive design*

**Phase 3: Validate & Harden (RIGOROUS)**
```
/cognitive_class rigorous
Review this payment processing code for security issues.
```
*Result: All vulnerabilities identified*

**Phase 4: Implement Quick Version (FAST)**
```
/cognitive_class fast
Quick checklist: does the code compile, tests pass, deployment ready?
```
*Result: Quick validation before deployment*

---

### Workflow 2: Complex Problem Solving

```
/cognitive_class standard
I have a performance issue. Database queries are slow on this table.
[describe table structure and queries]

=> Get balanced analysis of likely issues
```

If issue is complex:
```
/cognitive_class deep
Let's dive deeper into this database performance problem.
What architectural changes might help?
```

If needs validation:
```
/cognitive_class rigorous
Before we deploy this database optimization, what could go wrong?
```

---

### Workflow 3: Learning & Research

**Topic: Distributed Systems**
```
/cognitive_class deep
Explain consensus algorithms in distributed systems.
What are the trade-offs between Raft and Paxos?
```

**Deep dive on specific algorithm:**
```
/cognitive_class deep
Walk me through how Raft handles leader election and log replication.
What are the failure scenarios and how are they handled?
```

---

## Advanced Usage Patterns

### Pattern 1: Multi-Pass Analysis

```
# First pass: STANDARD (quick overview)
/cognitive_class standard
What's the best way to implement a caching layer?

# Second pass: DEEP (detailed analysis)
/cognitive_class deep
Now let's explore this caching strategy in depth.
What are the pitfalls and how to avoid them?

# Third pass: RIGOROUS (validate for production)
/cognitive_class rigorous
Before we deploy this caching solution, what could break?
How do we handle cache invalidation edge cases?
```

### Pattern 2: Balanced Team Decision Making

**For initial exploration:**
```
/cognitive_class creative
What innovative approaches could solve this problem?
```

**For practical evaluation:**
```
/cognitive_class standard
Which of these approaches is most practical for our constraints?
```

**For final vetting:**
```
/cognitive_class rigorous
What are the risks of the chosen approach?
```

### Pattern 3: Quality-Speed Optimization

**When you need speed:**
```
/cognitive_class fast
Give me the quick solution to [problem]
```

**When you need quality:**
```
/cognitive_class deep
Thoroughly analyze [problem] and provide comprehensive solution
```

**When you need both:**
```
/cognitive_class standard
Analyze [problem] with good balance of speed and quality
```

---

## Task Complexity Guidelines

### Simple Tasks (Use FAST)
- Lookup facts
- Simple calculations
- Pattern matching
- Quick clarifications
- Format conversion
- Single-factor decisions

**Example:**
```
/cognitive_class fast
Convert 5MB to bytes
```

### Moderate Tasks (Use STANDARD)
- Bug fixing
- Code reviews
- API design
- Database schema
- Implementation planning
- Technical explanations

**Example:**
```
/cognitive_class standard
Design a REST API for a blog platform
```

### Complex Tasks (Use DEEP)
- System architecture
- High-level strategy
- Research topics
- Novel solutions
- Trade-off analysis
- Long-term planning

**Example:**
```
/cognitive_class deep
Design a real-time collaboration system for 100K concurrent users
```

### Creative Tasks (Use CREATIVE)
- Ideation sessions
- Feature brainstorming
- Problem reframing
- Novel approaches
- Innovation exploration

**Example:**
```
/cognitive_class creative
What are unexpected use cases for blockchain technology?
```

### Safety-Critical Tasks (Use RIGOROUS)
- Security review
- Financial logic
- Healthcare systems
- Privacy implementation
- Compliance verification
- Vulnerability assessment

**Example:**
```
/cognitive_class rigorous
Review this implementation of OAuth 2.0 for security flaws
```

---

## Switching Between Classes

### Manual Switching

```
/cognitive_class fast          # Switch immediately
[question]                     # Ask question
```

### Recommended Switching

```
/cognitive_class recommend "api design"  # Get recommendation
=> Output: recommended: STANDARD

/cognitive_class standard               # Switch to recommendation
[question about API design]
```

### Viewing Current Class

```
/cognitive_class current       # See which class is active
=> Current: STANDARD
```

### Viewing Class Details

```
/cognitive_class info deep     # Show DEEP class details
=> Reasoning Depth: 4
=> Token Multiplier: 1.5x
=> Best for: [list]
=> Instructions: [behavior guidelines]
```

---

## Command Reference

### Switching Classes
```bash
/cognitive_class fast              # Switch to FAST
/cognitive_class standard          # Switch to STANDARD (default)
/cognitive_class deep              # Switch to DEEP
/cognitive_class creative          # Switch to CREATIVE
/cognitive_class rigorous          # Switch to RIGOROUS
```

### Information
```bash
/cognitive_class list              # Show all available classes
/cognitive_class current           # Show current active class
/cognitive_class info fast         # Show details for FAST class
/cognitive_class recommend task    # Get recommendation for task type
```

### Analysis
```bash
/cognitive_class history           # Show class switching history
/cognitive_class stats             # Show usage statistics
```

---

## Token Budget Impact

Different classes use different amounts of tokens due to reasoning depth:

| Class | Multiplier | Impact | Tokens for typical answer |
|-------|-----------|--------|---------------------------|
| FAST | 0.5x | Lowest cost | ~500 tokens |
| STANDARD | 1.0x | Baseline | ~1000 tokens |
| CREATIVE | 1.2x | +20% | ~1200 tokens |
| RIGOROUS | 1.2x | +20% | ~1200 tokens |
| DEEP | 1.5x | Highest cost | ~1500 tokens |

**Strategy:** Use FAST for simple tasks to save tokens, DEEP only when needed for complex problems.

---

## Best Practices

1. **Match class to task complexity**
   - Don't use DEEP for trivial questions
   - Don't use FAST for complex architecture

2. **Use recommendations when uncertain**
   ```
   /cognitive_class recommend "my task description"
   ```

3. **Chain classes for multi-phase work**
   - CREATIVE → DEEP → RIGOROUS workflow

4. **Monitor token usage**
   - Simple tasks: use FAST (0.5x)
   - Complex tasks: use DEEP (1.5x)

5. **Consider your constraints**
   - Budget tight? Use FAST/STANDARD
   - Quality critical? Use RIGOROUS
   - Novel solution needed? Use CREATIVE
   - Uncertain? Use STANDARD

---

## Troubleshooting

**Q: Response isn't detailed enough**
- A: Switch to DEEP class
- ```
  /cognitive_class deep
  [re-ask question]
  ```

**Q: Response is too verbose/slow**
- A: Switch to FAST or STANDARD
- ```
  /cognitive_class fast
  [ask simplified question]
  ```

**Q: Need security review**
- A: Always use RIGOROUS for security-critical code
- ```
  /cognitive_class rigorous
  Review this code for vulnerabilities
  ```

**Q: Want creative solutions**
- A: Use CREATIVE class
- ```
  /cognitive_class creative
  What innovative approaches could solve this?
  ```

**Q: Uncertain which class to use**
- A: Use recommendation system
- ```
  /cognitive_class recommend "describe your task"
  ```

---

## Summary

The cognitive classes system provides a way to optimize your interactions based on task type:

- **FAST** for speed
- **STANDARD** for balance
- **DEEP** for complexity
- **CREATIVE** for innovation
- **RIGOROUS** for safety

Choose wisely to maximize quality and efficiency!
