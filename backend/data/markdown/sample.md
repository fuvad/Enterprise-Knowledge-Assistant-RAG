# Authentication

## JSON Web Tokens

Authentication is commonly implemented using JSON Web Tokens. After a successful login, the server issues an access token to the client. The client includes this token in future requests. JWTs are stateless and can be verified without storing session data on the server.

## Access Tokens

Access tokens are short-lived credentials used to authorize requests. They typically expire after a predefined period. Short expiration times reduce security risks if a token is compromised. Applications often validate tokens on every request.

## Refresh Tokens

Refresh tokens allow users to obtain new access tokens without logging in again. They are usually stored more securely than access tokens. Refresh tokens often have longer lifetimes and may be revoked independently.

## Password Hashing

Passwords should never be stored in plain text. Modern systems use hashing algorithms such as bcrypt or Argon2. Hashing converts passwords into irreversible values. Even if a database is compromised, hashes help protect user credentials.

## Multi Factor Authentication

Multi factor authentication requires users to provide multiple forms of verification. Common factors include passwords, mobile authenticator codes, and hardware security keys. MFA significantly reduces the risk of account compromise.

## Authorization

Authentication verifies identity while authorization determines permissions. Role based access control is commonly used in enterprise systems. Users may belong to groups that define what resources they can access.

## Audit Logging

Security systems record authentication events in audit logs. These logs track successful logins, failed login attempts, and privilege changes. Audit records support compliance and security investigations.

## Session Revocation

Organizations sometimes need to invalidate active sessions. Session revocation can be implemented using token blacklists. Revoked tokens are rejected even if they have not yet expired.

## Password Recovery

Password reset workflows allow users to regain account access. Reset links should expire after a short period. Systems often require email verification before permitting password changes.

## Identity Management

Identity management systems maintain user profiles and credentials. Large organizations frequently integrate identity providers with multiple applications. Centralized identity management simplifies administration and security monitoring.

# Cooking

## Healthy Ingredients

Healthy meals often include vegetables, fruits, legumes, and whole grains. Nutrient rich ingredients contribute to balanced diets. Fresh ingredients generally provide better flavor and texture.

## Mediterranean Cuisine

Mediterranean cuisine emphasizes olive oil, vegetables, fish, and herbs. Many recipes rely on fresh ingredients rather than processed foods. This style of cooking is associated with several health benefits.

## Pasta Preparation

Pasta is typically cooked in salted boiling water. Different pasta shapes pair well with different sauces. Timing is important because overcooked pasta can become soft and lose texture.

## Baking Basics

Baking requires precise measurements and controlled temperatures. Small changes in ingredient ratios can significantly affect results. Bakers often use scales to improve consistency.

## Bread Making

Bread dough must be kneaded to develop gluten structure. After kneading, dough usually rests to allow fermentation. Proper fermentation contributes to flavor and texture.

## Herbs and Spices

Herbs contribute aroma while spices add both flavor and color. Basil, rosemary, and thyme are commonly used herbs. Spices such as cumin and paprika create distinctive flavor profiles.

## Food Safety

Kitchen safety is essential during food preparation. Raw meats should be handled carefully to prevent contamination. Proper handwashing reduces foodborne illness risks.

## Grilling

Grilling exposes food to direct heat. This cooking method creates unique flavors and textures. Many grilled foods develop a characteristic smoky taste.

## Soups and Stews

Soups and stews can be prepared using seasonal vegetables and proteins. Slow cooking allows flavors to blend over time. Different cultures have developed distinctive soup traditions.

## Restaurant Operations

Restaurants depend on efficient kitchen workflows. Chefs coordinate food preparation, inventory management, and quality control. Successful restaurants balance consistency with creativity.

# Astronomy

## Stars

Stars are massive spheres of plasma powered by nuclear fusion. They produce light and heat through energy generating reactions. The Sun is the closest star to Earth.

## Galaxies

Galaxies contain billions of stars, gas clouds, and dark matter. Spiral galaxies have rotating disk structures. Elliptical galaxies have more rounded shapes.

## Black Holes

Black holes possess extremely strong gravitational fields. Nothing can escape once it crosses the event horizon. Scientists study black holes through their effects on nearby matter.

## Telescopes

Telescopes collect electromagnetic radiation from distant objects. Optical telescopes gather visible light. Radio telescopes detect radio signals originating in space.

## Exoplanets

Exoplanets orbit stars outside our solar system. Thousands of exoplanets have been discovered. Researchers analyze these worlds to understand planetary formation.

## Spectroscopy

Spectroscopy allows scientists to determine chemical composition. Different elements produce distinct spectral signatures. Astronomers use spectroscopy to study stars and galaxies.

## Dark Matter

Dark matter does not emit light and cannot be directly observed. Evidence for dark matter comes from gravitational effects. Its exact nature remains unknown.

## Space Missions

Space missions expand scientific understanding of the universe. Robotic spacecraft explore planets, moons, and asteroids. Observational missions collect large quantities of scientific data.

## Astrophysics

Astrophysics applies physical laws to astronomical phenomena. Researchers investigate gravity, radiation, and cosmic evolution. The field connects astronomy with physics and mathematics.

## International Collaboration

Modern astronomy depends on international cooperation. Scientists share observational data and research findings. Large observatories and space projects often involve multiple countries.
