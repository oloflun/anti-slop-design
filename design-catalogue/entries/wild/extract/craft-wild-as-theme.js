// React Theme — extracted from https://craft.wild.as/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    accent: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
 *   };
 *   fonts: {
    body: string;
    mono: string;
 *   };
 *   fontSizes: {
    '14': string;
    '15': string;
    '16': string;
    '22': string;
    '34': string;
    '66.56': string;
    '43.52': string;
    '28.16': string;
    '18.56': string;
    '15.36': string;
    '14.5': string;
    '13.5': string;
 *   };
 *   space: {
    '1': string;
    '12': string;
    '26': string;
    '35': string;
    '42': string;
    '49': string;
    '56': string;
    '98': string;
    '126': string;
    '168': string;
    '356': string;
 *   };
 *   radii: {
    md: string;
 *   };
 *   shadows: {
    md: string;
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
    "primary": "#d8ff00",
    "secondary": "#f5c518",
    "accent": "#6c4cf1",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#ffffff",
    "neutral100": "#0a0a0a",
    "neutral200": "#2a2a2a",
    "neutral300": "#000000",
    "neutral400": "#8b8b8b"
  },
  "fonts": {
    "body": "'Times New Roman', sans-serif",
    "mono": "'SFMono-Regular', monospace"
  },
  "fontSizes": {
    "14": "14px",
    "15": "15px",
    "16": "16px",
    "22": "22px",
    "34": "34px",
    "66.56": "66.56px",
    "43.52": "43.52px",
    "28.16": "28.16px",
    "18.56": "18.56px",
    "15.36": "15.36px",
    "14.5": "14.5px",
    "13.5": "13.5px"
  },
  "space": {
    "1": "1px",
    "12": "12px",
    "26": "26px",
    "35": "35px",
    "42": "42px",
    "49": "49px",
    "56": "56px",
    "98": "98px",
    "126": "126px",
    "168": "168px",
    "356": "356px"
  },
  "radii": {
    "md": "10px"
  },
  "shadows": {
    "md": "rgba(10, 10, 10, 0.14) 0px 2px 12px 0px"
  },
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
    "primary": {
      "main": "#d8ff00",
      "light": "hsl(69, 100%, 65%)",
      "dark": "hsl(69, 100%, 35%)"
    },
    "secondary": {
      "main": "#f5c518",
      "light": "hsl(47, 92%, 68%)",
      "dark": "hsl(47, 92%, 38%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#0a0a0a"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0a0a0a"
    }
  },
  "typography": {
    "fontFamily": "'SFMono-Regular', sans-serif",
    "h1": {
      "fontSize": "34px",
      "fontWeight": "400",
      "lineHeight": "34px"
    },
    "h2": {
      "fontSize": "28.16px",
      "fontWeight": "500",
      "lineHeight": "42.24px"
    },
    "h3": {
      "fontSize": "22px",
      "fontWeight": "400",
      "lineHeight": "33px"
    },
    "body1": {
      "fontSize": "18.56px",
      "fontWeight": "400",
      "lineHeight": "21.9008px"
    }
  },
  "shape": {
    "borderRadius": 6
  },
  "shadows": [
    "rgba(10, 10, 10, 0.14) 0px 2px 12px 0px"
  ]
};

export default theme;
