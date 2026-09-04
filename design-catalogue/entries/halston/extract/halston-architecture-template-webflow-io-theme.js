// React Theme — extracted from https://halston-architecture-template.webflow.io/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
 *   };
 *   fonts: {
    body: string;
    mono: string;
 *   };
 *   fontSizes: {
    '30': string;
    '56': string;
    '192': string;
    '115.2': string;
    '102.4': string;
    '51.2': string;
    '40.8': string;
    '38.4': string;
    '26.4': string;
    '25.6': string;
    '20.4': string;
    '19.2': string;
 *   };
 *   space: {
    '3': string;
    '42': string;
    '48': string;
    '64': string;
    '80': string;
    '96': string;
    '115': string;
    '192': string;
    '320': string;
    '483': string;
 *   };
 *   radii: {
    sm: string;
    full: string;
 *   };
 *   shadows: {

 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "background": "#583939",
    "foreground": "#000000",
    "neutral50": "#583939",
    "neutral100": "#000000",
    "neutral200": "#ffffff",
    "neutral300": "#99988f"
  },
  "fonts": {
    "body": "'General Sans', sans-serif",
    "mono": "'JetBrains Mono', monospace"
  },
  "fontSizes": {
    "30": "30px",
    "56": "56px",
    "192": "192px",
    "115.2": "115.2px",
    "102.4": "102.4px",
    "51.2": "51.2px",
    "40.8": "40.8px",
    "38.4": "38.4px",
    "26.4": "26.4px",
    "25.6": "25.6px",
    "20.4": "20.4px",
    "19.2": "19.2px"
  },
  "space": {
    "3": "3px",
    "42": "42px",
    "48": "48px",
    "64": "64px",
    "80": "80px",
    "96": "96px",
    "115": "115px",
    "192": "192px",
    "320": "320px",
    "483": "483px"
  },
  "radii": {
    "sm": "3px",
    "full": "50px"
  },
  "shadows": {},
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "background": {
      "default": "#583939",
      "paper": "#583939"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#583939"
    }
  },
  "typography": {
    "fontFamily": "'JetBrains Mono', sans-serif",
    "h1": {
      "fontSize": "40.8px",
      "fontWeight": "500",
      "lineHeight": "40.8px"
    }
  },
  "shape": {
    "borderRadius": 3
  },
  "shadows": []
};

export default theme;
